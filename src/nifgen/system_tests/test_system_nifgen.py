import nifgen
import pytest


@pytest.fixture(scope='function')
def session():
    with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5433 (2CH);BoardType:PXIe') as simulated_session:
        yield simulated_session


def test_self_test(session):
    result, message = session.self_test()
    assert result == 0
    assert message == 'Self test passed'


def test_get_attribute_string(session):
    model = session.instrument_model
    assert model == 'NI PXIe-5433 (2CH)'


def test_error_message(session):
    # Calling the private function directly, as _get_error_message() only gets called when you have an invalid session,
    # and there is no good way for us to invalidate a simulated session.
    message = session._error_message(-1074135027)
    assert message.find('Attribute is read-only.') != -1


def test_get_error(session):
    try:
        session.instrument_model = ''
        assert False
    except nifgen.Error as e:
        assert e.code == -1074135027  # Error : Attribute is read-only.
        assert e.description.find('Attribute is read-only.') != -1


def test_method_get_self_cal_supported(session):
    assert session.get_self_cal_supported() in [True, False]


def test_get_self_cal_last_date_and_time():
    try:
        with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5421;BoardType:PXI') as session:  # Simulated 5433 returns unrecoverable error when calling get_self_cal_last_date_and_time()
            year, month, day, hour, minute = session.get_self_cal_last_date_and_time()
            assert False
    except nifgen.Error as e:
        assert e.code == -1074118632  # This operation is not supported for simulated device


def test_self_cal(session):
        session.self_cal()


def test_standard_waveform(session):
    session.output_mode = nifgen.OutputMode.FUNC
    session.configure_standard_waveform(nifgen.Waveform.SINE, 2.0, 2000000, 1.0, 0.0)
    expected_frequency = 2000000
    with session.initiate():
        assert session.func_amplitude == 2.0
        assert session.func_waveform == nifgen.Waveform.SINE
        actual_frequency = session.func_frequency
        in_range = abs(actual_frequency - expected_frequency) <= max(1e-09 * max(abs(actual_frequency), abs(expected_frequency)), 0.0)   # https://stackoverflow.com/questions/5595425/what-is-the-best-way-to-compare-floats-for-almost-equality-in-python
        assert in_range is True
        assert session.func_dc_offset == 1.0
        assert session.func_start_phase == 0.0
        assert session.is_done() is False


def test_frequency_list(session):
    session.output_mode = nifgen.OutputMode.FREQ_LIST
    duration_array = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
    frequency_array = [1000, 100900, 200800, 300700, 400600, 500500, 600400, 700300, 800200, 900100]
    waveform_handle = session.create_freq_list(nifgen.Waveform.SQUARE, frequency_array, duration_array)
    session.configure_freq_list(waveform_handle, 2.0, 0, 0)
    session.trigger_mode = nifgen.TriggerMode.CONTINUOUS
    session.output_enabled = True
    assert session.func_waveform == nifgen.Waveform.SQUARE
    assert session.func_amplitude == 2.0


def test_clear_freq_list(session):
    session.clear_freq_list(-1)


def test_configure_arb_waveform(session):
    waveform_data = [0.000000, 0.049068, 0.098017, 0.146730, 0.195090, 0.242980, 0.290285, 0.336890, 0.382683, 0.427555]
    session.output_mode = nifgen.OutputMode.ARB
    session.configure_arb_waveform(session.create_waveform_f64(waveform_data), 1.0, 0.0)


def test_disable(session):
    channel = session['0']
    assert channel.output_enabled is True
    session.disable()
    assert channel.output_enabled is False


def test_get_ext_cal_last_date_and_time():
    with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5421;BoardType:PXI') as session:  # 5433 throws out unrecoverable error on calling get_ext_cal_last_date_and_time()
        try:
            session.get_ext_cal_last_date_and_time()
            assert False
        except nifgen.Error as e:
            assert e.code == -1074118632  # This operation is not supported for simulated device


def test_get_ext_cal_last_temp(session):
    try:
        session.get_ext_cal_last_temp()
    except nifgen.Error as e:
        assert e.code == -1074135023  # Function or method not supported for 5413/23/33 and not supported on any other FGen when simulated


def test_get_ext_cal_recommended_interval(session):
    recommended_interval = session.get_ext_cal_recommended_interval()
    assert recommended_interval == 24  # recommended external cal interval is 24 months


''' TODO(Jaleel) Enable after Issue#558 fixed
def test_get_hardware_state():
    with nifgen.Session('', False, 'Simulate=1, DriverSetup=Model:5421;BoardType:PXI') as session:  # Function or method not supported for 5413/23/33
        assert session.get_hardware_state() == nifgen.HardwareState.IDLE
'''


def test_get_self_cal_last_temp(session):
    assert session.get_self_cal_last_temp() == 0.0  # returns 0.0 for a simulated 5433


def test_query_arb_wfm_capabilities(session):
    max_number_of_waveform, waveform_quantum, minimum_waveform_size, maximum_waveform_size = session.query_arb_wfm_capabilities()
    assert max_number_of_waveform == 4194304  # default values for max_number_of_waveform, waveform_quantum, minimum_waveform_size, maximum_waveform_size for a simulated 5433 is 4194304, 1, 4, 268435456 respectively
    assert waveform_quantum == 1
    assert minimum_waveform_size == 4
    assert maximum_waveform_size == 268435456


def test_query_freq_list_capabilities(session):
    maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum = session.query_freq_list_capabilities()  # comparing with default values for simulated 5433
    assert maximum_number_of_freq_lists == 9999
    assert minimum_frequency_list_length == 1
    assert maximum_frequency_list_length == 1024
    assert minimum_frequency_list_duration == 1e-08
    assert maximum_frequency_list_duration == 2814749.76711
    assert frequency_list_duration_quantum == 1e-08


def test_read_current_temperature(session):
    assert session.read_current_temperature() > 25.0
