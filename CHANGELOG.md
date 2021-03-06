# Changelog

* [Unreleased](#unreleased)
* [0.4.0](#040---2017-11-07)
* [0.3.0](#030---2017-10-13)
* [0.2.0](#020---2017-09-20)
* [0.1.0](#010---2017-09-01)

All notable changes to this project will be documented in this file.

## [Unreleased]
* ### ALL
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-DMM
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-ModInst
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-Switch
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-DCPower
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-FGEN
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-SCOPE
  * #### Added
    * Initial release
  * #### Changed
  * #### Removed
    * Removed Peer to Peer attributes

## 0.4.0 - 2017-11-07
* ### ALL
  * #### Changed
    * Simplified examples by removing try/except
    * **SOURCE BREAKER:** Changed names of enum value names to correspond to C #defines
* ### NI-DMM
  * #### Changed
    * Removed incorrect leading underscore from some enum values:
      * Function.AC_VOLTS_DC_COUPLED
      * Function.WAVEFORM_CURRENT
      * MeasurementCompleteDest.LBR_TRIG_0
      * OperationMode.IVIDMM_MODE
      * SampleTrigger.EXTERNAL
      * SampleTrigger.TTL_3
      * TriggerSource.TTL_0
      * TriggerSource.TTL_3
      * TriggerSource.TTL_7
      * TriggerSource.PXI_STAR
* ### NI-Switch
  * #### Removed
    * Support for is_debounced and is_scanning functions. Instead use the attribute of the same name.
* ### NI-DCPower
  * #### Added
    * New example nidcpower_advanced_sequence.py
  * #### Changed
    * Fixed method signature for:
      * wait_for_event
      * create_sequence
      * create_advanced_sequence
  * #### Removed
    * Support for measure_multiple until issue #444 is addressed.
* ### NI-FGEN
  * #### Added
    * Initial release

## 0.3.0 - 2017-10-13
* ### ALL
  * #### Added
    * Support for ViInt64 (64-bit integers)
  * #### Changed
    * Modified how methods with repeated capabilities are invoked. There's no longer (for example) a "channel_name" input. Instead:
      ```python
      # Sets sequence on channels 0 through 3
      session['0-3'].set_sequence(values, source_delays)
      ```
    * Enum value documentation lists the fully qualified name - this is to allow easy copy/paste
* ### NI-DMM
  * #### Changed
    * Added default values to some parameters.
  * #### Removed
    * Removed methods that aren’t useful in the Python bindings.
* ### NI-SWITCH
  * #### Changed
    * Added default values to some parameters.
  * #### Removed
    * Removed methods that aren’t useful in the Python bindings.
* ### NI-DCPower
  * #### Added
    * Initial release

## 0.2.0 - 2017-09-20
* ### ALL
  * #### Added
    * Suport for channel-based properties
  * #### Changed
    * Warnings no longer raise an exception
      * Warnings are now added to warnings.warn()
* ### NI-DMM
  * #### Changed
    * Added support for enums with types other than ViInt32 (Fixes [#330](https://github.com/ni/nimi-python/issues/330))
* ### NI-ModInst
  * #### Changed
    * Device index is now on session not attribute. The correct way is now
      ```python
      i = 0
      with nimodinst.Session('nidmm') as session:
          name = session[i].device_name
      ```
* ### NI-SWITCH
  * #### Added
    * Initial release

## 0.1.0 - 2017-09-01
* ### NI-DMM
  * #### Added
    * Initial release
* ### NI-ModInst
  * #### Added
    * Initial release

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Python Versioning](http://legacy.python.org/dev/peps/pep-0396/).

<!--
## [Unreleased]
* ### ALL
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-DMM
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-ModInst
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-Switch
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-DCPower
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-FGEN
  * #### Added
  * #### Changed
  * #### Removed
* ### NI-SCOPE
  * #### Added
  * #### Changed
  * #### Removed
-->

