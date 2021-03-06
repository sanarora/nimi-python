# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitializeWithChannels':          { 'codegen_method': 'private',  },
    'InitWithOptions':                 { 'codegen_method': 'no',       },
    'Initiate':                        { 'codegen_method': 'private',  },
    'close':                           { 'codegen_method': 'private',  },
    'Abort':                           { 'codegen_method': 'private',  },
    '.etAttribute.+':                  { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                            { 'codegen_method': 'no',       },
    'error_message':                   { 'codegen_method': 'private',  },
    'GetError':                        { 'codegen_method': 'private',  },
    'ClearError':                      { 'codegen_method': 'no',       },
    'LockSession':                     { 'codegen_method': 'no',       },
    'UnlockSession':                   { 'codegen_method': 'no',       },
    '.+ExtCal':                        { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalAdjust.+':                     { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalSelfCalibrate':                { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'ConnectInternalReference':        { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    '.+UserDefined.+':                 { 'codegen_method': 'no',       },
    'SetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetNextInterchangeWarning':       { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':        { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'error_query':                     { 'codegen_method': 'no',       },
    'ConfigureAutoZero':               { 'codegen_method': 'no',       },
    'ConfigureCurrent.+':              { 'codegen_method': 'no',       },
    'ConfigureOutput.+':               { 'codegen_method': 'no',       },
    'ConfigurePowerLineFrequency':     { 'codegen_method': 'no',       },
    'ConfigurePulse.+':                { 'codegen_method': 'no',       },
    'ConfigureSense':                  { 'codegen_method': 'no',       },
    'ConfigureVoltageL.+':             { 'codegen_method': 'no',       },
    'ConfigureSourceMode':             { 'codegen_method': 'no',       },
    'ConfigureSoftwareEdge.+Trigger':  { 'codegen_method': 'no',       },
    'Disable.+Trigger':                { 'codegen_method': 'no',       },
    'revision_query':                  { 'codegen_method': 'no',       },
    'MeasureMultiple':                 { 'codegen_method': 'no',       },  # Issue 444
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'ConfigureAutoZero':                            { 'parameters': { 2: { 'enum': 'AutoZero',                    }, }, },
    'ConfigureApertureTime':                        { 'parameters': { 3: { 'enum': 'ApertureTimeUnits',           }, }, },
    'ConfigureDigitalEdgeMeasureTrigger':           { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'ConfigureDigitalEdgePulseTrigger':             { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'ConfigureDigitalEdgeSequenceAdvanceTrigger':   { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'ConfigureDigitalEdgeSourceTrigger':            { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'ConfigureDigitalEdgeStartTrigger':             { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'SendSoftwareEdgeTrigger':                      { 'parameters': { 1: { 'enum': 'SendSoftwareEdgeTriggerType', }, }, },
    'WaitForEvent':                                 { 'parameters': { 1: { 'enum': 'Event',                       }, }, },
    'Measure':                                      { 'parameters': { 2: { 'enum': 'MeasurementTypes',            }, }, },
    'QueryOutputState':                             { 'parameters': { 2: { 'enum': 'OutputStates',                }, }, },
    # @TODO add all enums
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'BufferSize'}, }, }, },
    'self_test':                    { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':         { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetCalUserDefinedInfo':        { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'error_message':                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetChannelName':               { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'SetSequence':                  { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'Size'}, }, }, },
    'CreateAdvancedSequence':       { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'attributeIdCount'}, }, }, },
    'FetchMultiple':                { 'parameters': { 4: { 'size': {'mechanism':'passed-in', 'value':'Count'}, },
                                                      5: { 'size': {'mechanism':'passed-in', 'value':'Count'}, },
                                                      6: { 'size': {'mechanism':'passed-in', 'value':'Count'}, }, }, },
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'error_message':                { 'is_error_handling': True },
    'GetError':                     { 'is_error_handling': True },
}

# Default values for method parameters
functions_default_value = {
    'InitializeWithChannels':                        { 'parameters': { 1: { 'default_value': '', },
                                                                       2: { 'default_value': False, },
                                                                       3: { 'default_value': '', }, }, },
    'ConfigureApertureTime':                         { 'parameters': { 3: { 'default_value': 'ApertureTimeUnits.SECONDS', }, }, },
    'SetSequence':                                   { 'parameters': { 2: { 'default_value': None, }, }, },
    'ConfigureDigitalEdgeMeasureTrigger':            { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'ConfigureDigitalEdgePulseTrigger':              { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'ConfigureDigitalEdgeSequenceAdvanceTrigger':    { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'ConfigureDigitalEdgeSourceTrigger':             { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'ConfigureDigitalEdgeStartTrigger':              { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'CreateAdvancedSequence':                        { 'parameters': { 4: { 'default_value': True, }, }, },
    'CreateAdvancedSequenceStep':                    { 'parameters': { 1: { 'default_value': True, }, }, },
    'ExportSignal':                                  { 'parameters': { 2: { 'default_value': '', }, }, },
    'SendSoftwareEdgeTrigger':                       { 'parameters': { 1: { 'default_value': 'SendSoftwareEdgeTriggerType.START', }, }, },
    'WaitForEvent':                                  { 'parameters': { 2: { 'default_value': 10.0, },}, },
    'FetchMultiple':                                 { 'parameters': { 1: { 'default_value': 1.0, },
                                                                       2: { 'default_value': 1.0, }, }, },

}

