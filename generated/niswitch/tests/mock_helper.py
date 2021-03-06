# This file was generated


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['AbortScan'] = {}
        self._defaults['AbortScan']['return'] = 0
        self._defaults['CanConnect'] = {}
        self._defaults['CanConnect']['return'] = 0
        self._defaults['CanConnect']['pathCapability'] = None
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureScanList'] = {}
        self._defaults['ConfigureScanList']['return'] = 0
        self._defaults['ConfigureScanTrigger'] = {}
        self._defaults['ConfigureScanTrigger']['return'] = 0
        self._defaults['Connect'] = {}
        self._defaults['Connect']['return'] = 0
        self._defaults['ConnectMultiple'] = {}
        self._defaults['ConnectMultiple']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['Disconnect'] = {}
        self._defaults['Disconnect']['return'] = 0
        self._defaults['DisconnectAll'] = {}
        self._defaults['DisconnectAll']['return'] = 0
        self._defaults['DisconnectMultiple'] = {}
        self._defaults['DisconnectMultiple']['return'] = 0
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['channelNameBuffer'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['Code'] = None
        self._defaults['GetError']['Description'] = None
        self._defaults['GetPath'] = {}
        self._defaults['GetPath']['return'] = 0
        self._defaults['GetPath']['Path'] = None
        self._defaults['GetRelayCount'] = {}
        self._defaults['GetRelayCount']['return'] = 0
        self._defaults['GetRelayCount']['relayCount'] = None
        self._defaults['GetRelayName'] = {}
        self._defaults['GetRelayName']['return'] = 0
        self._defaults['GetRelayName']['relayNameBuffer'] = None
        self._defaults['GetRelayPosition'] = {}
        self._defaults['GetRelayPosition']['return'] = 0
        self._defaults['GetRelayPosition']['relayPosition'] = None
        self._defaults['InitWithTopology'] = {}
        self._defaults['InitWithTopology']['return'] = 0
        self._defaults['InitWithTopology']['vi'] = None
        self._defaults['InitiateScan'] = {}
        self._defaults['InitiateScan']['return'] = 0
        self._defaults['RelayControl'] = {}
        self._defaults['RelayControl']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['RouteScanAdvancedOutput'] = {}
        self._defaults['RouteScanAdvancedOutput']['return'] = 0
        self._defaults['RouteTriggerInput'] = {}
        self._defaults['RouteTriggerInput']['return'] = 0
        self._defaults['SendSoftwareTrigger'] = {}
        self._defaults['SendSoftwareTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetContinuousScan'] = {}
        self._defaults['SetContinuousScan']['return'] = 0
        self._defaults['SetPath'] = {}
        self._defaults['SetPath']['return'] = 0
        self._defaults['WaitForDebounce'] = {}
        self._defaults['WaitForDebounce']['return'] = 0
        self._defaults['WaitForScanComplete'] = {}
        self._defaults['WaitForScanComplete']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niSwitch_AbortScan(self, vi):  # noqa: N802
        if self._defaults['AbortScan']['return'] != 0:
            return self._defaults['AbortScan']['return']
        return self._defaults['AbortScan']['return']

    def niSwitch_CanConnect(self, vi, channel1, channel2, path_capability):  # noqa: N802
        if self._defaults['CanConnect']['return'] != 0:
            return self._defaults['CanConnect']['return']
        if self._defaults['CanConnect']['pathCapability'] is None:
            raise MockFunctionCallError("niSwitch_CanConnect", param='pathCapability')
        path_capability.contents.value = self._defaults['CanConnect']['pathCapability']
        return self._defaults['CanConnect']['return']

    def niSwitch_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niSwitch_ConfigureScanList(self, vi, scanlist, scan_mode):  # noqa: N802
        if self._defaults['ConfigureScanList']['return'] != 0:
            return self._defaults['ConfigureScanList']['return']
        return self._defaults['ConfigureScanList']['return']

    def niSwitch_ConfigureScanTrigger(self, vi, scan_delay, trigger_input, scan_advanced_output):  # noqa: N802
        if self._defaults['ConfigureScanTrigger']['return'] != 0:
            return self._defaults['ConfigureScanTrigger']['return']
        return self._defaults['ConfigureScanTrigger']['return']

    def niSwitch_Connect(self, vi, channel1, channel2):  # noqa: N802
        if self._defaults['Connect']['return'] != 0:
            return self._defaults['Connect']['return']
        return self._defaults['Connect']['return']

    def niSwitch_ConnectMultiple(self, vi, connection_list):  # noqa: N802
        if self._defaults['ConnectMultiple']['return'] != 0:
            return self._defaults['ConnectMultiple']['return']
        return self._defaults['ConnectMultiple']['return']

    def niSwitch_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niSwitch_Disconnect(self, vi, channel1, channel2):  # noqa: N802
        if self._defaults['Disconnect']['return'] != 0:
            return self._defaults['Disconnect']['return']
        return self._defaults['Disconnect']['return']

    def niSwitch_DisconnectAll(self, vi):  # noqa: N802
        if self._defaults['DisconnectAll']['return'] != 0:
            return self._defaults['DisconnectAll']['return']
        return self._defaults['DisconnectAll']['return']

    def niSwitch_DisconnectMultiple(self, vi, disconnection_list):  # noqa: N802
        if self._defaults['DisconnectMultiple']['return'] != 0:
            return self._defaults['DisconnectMultiple']['return']
        return self._defaults['DisconnectMultiple']['return']

    def niSwitch_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niSwitch_GetAttributeViBoolean", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niSwitch_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niSwitch_GetAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niSwitch_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niSwitch_GetAttributeViReal64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niSwitch_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niSwitch_GetAttributeViString", param='attributeValue')
        if array_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niSwitch_GetChannelName(self, vi, index, buffer_size, channel_name_buffer):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        if self._defaults['GetChannelName']['channelNameBuffer'] is None:
            raise MockFunctionCallError("niSwitch_GetChannelName", param='channelNameBuffer')
        if buffer_size.value == 0:
            return len(self._defaults['GetChannelName']['channelNameBuffer'])
        channel_name_buffer.value = self._defaults['GetChannelName']['channelNameBuffer'].encode('ascii')
        return self._defaults['GetChannelName']['return']

    def niSwitch_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        if self._defaults['GetError']['Code'] is None:
            raise MockFunctionCallError("niSwitch_GetError", param='Code')
        code.contents.value = self._defaults['GetError']['Code']
        if self._defaults['GetError']['Description'] is None:
            raise MockFunctionCallError("niSwitch_GetError", param='Description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['Description'])
        description.value = self._defaults['GetError']['Description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niSwitch_GetPath(self, vi, channel1, channel2, buffer_size, path):  # noqa: N802
        if self._defaults['GetPath']['return'] != 0:
            return self._defaults['GetPath']['return']
        if self._defaults['GetPath']['Path'] is None:
            raise MockFunctionCallError("niSwitch_GetPath", param='Path')
        if buffer_size.value == 0:
            return len(self._defaults['GetPath']['Path'])
        path.value = self._defaults['GetPath']['Path'].encode('ascii')
        return self._defaults['GetPath']['return']

    def niSwitch_GetRelayCount(self, vi, relay_name, relay_count):  # noqa: N802
        if self._defaults['GetRelayCount']['return'] != 0:
            return self._defaults['GetRelayCount']['return']
        if self._defaults['GetRelayCount']['relayCount'] is None:
            raise MockFunctionCallError("niSwitch_GetRelayCount", param='relayCount')
        relay_count.contents.value = self._defaults['GetRelayCount']['relayCount']
        return self._defaults['GetRelayCount']['return']

    def niSwitch_GetRelayName(self, vi, index, relay_name_buffer_size, relay_name_buffer):  # noqa: N802
        if self._defaults['GetRelayName']['return'] != 0:
            return self._defaults['GetRelayName']['return']
        if self._defaults['GetRelayName']['relayNameBuffer'] is None:
            raise MockFunctionCallError("niSwitch_GetRelayName", param='relayNameBuffer')
        if relay_name_buffer_size.value == 0:
            return len(self._defaults['GetRelayName']['relayNameBuffer'])
        relay_name_buffer.value = self._defaults['GetRelayName']['relayNameBuffer'].encode('ascii')
        return self._defaults['GetRelayName']['return']

    def niSwitch_GetRelayPosition(self, vi, relay_name, relay_position):  # noqa: N802
        if self._defaults['GetRelayPosition']['return'] != 0:
            return self._defaults['GetRelayPosition']['return']
        if self._defaults['GetRelayPosition']['relayPosition'] is None:
            raise MockFunctionCallError("niSwitch_GetRelayPosition", param='relayPosition')
        relay_position.contents.value = self._defaults['GetRelayPosition']['relayPosition']
        return self._defaults['GetRelayPosition']['return']

    def niSwitch_InitWithTopology(self, resource_name, topology, simulate, reset_device, vi):  # noqa: N802
        if self._defaults['InitWithTopology']['return'] != 0:
            return self._defaults['InitWithTopology']['return']
        if self._defaults['InitWithTopology']['vi'] is None:
            raise MockFunctionCallError("niSwitch_InitWithTopology", param='vi')
        vi.contents.value = self._defaults['InitWithTopology']['vi']
        return self._defaults['InitWithTopology']['return']

    def niSwitch_InitiateScan(self, vi):  # noqa: N802
        if self._defaults['InitiateScan']['return'] != 0:
            return self._defaults['InitiateScan']['return']
        return self._defaults['InitiateScan']['return']

    def niSwitch_RelayControl(self, vi, relay_name, relay_action):  # noqa: N802
        if self._defaults['RelayControl']['return'] != 0:
            return self._defaults['RelayControl']['return']
        return self._defaults['RelayControl']['return']

    def niSwitch_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niSwitch_RouteScanAdvancedOutput(self, vi, scan_advanced_output_connector, scan_advanced_output_bus_line, invert):  # noqa: N802
        if self._defaults['RouteScanAdvancedOutput']['return'] != 0:
            return self._defaults['RouteScanAdvancedOutput']['return']
        return self._defaults['RouteScanAdvancedOutput']['return']

    def niSwitch_RouteTriggerInput(self, vi, trigger_input_connector, trigger_input_bus_line, invert):  # noqa: N802
        if self._defaults['RouteTriggerInput']['return'] != 0:
            return self._defaults['RouteTriggerInput']['return']
        return self._defaults['RouteTriggerInput']['return']

    def niSwitch_SendSoftwareTrigger(self, vi):  # noqa: N802
        if self._defaults['SendSoftwareTrigger']['return'] != 0:
            return self._defaults['SendSoftwareTrigger']['return']
        return self._defaults['SendSoftwareTrigger']['return']

    def niSwitch_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niSwitch_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niSwitch_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niSwitch_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niSwitch_SetContinuousScan(self, vi, continuous_scan):  # noqa: N802
        if self._defaults['SetContinuousScan']['return'] != 0:
            return self._defaults['SetContinuousScan']['return']
        return self._defaults['SetContinuousScan']['return']

    def niSwitch_SetPath(self, vi, path_list):  # noqa: N802
        if self._defaults['SetPath']['return'] != 0:
            return self._defaults['SetPath']['return']
        return self._defaults['SetPath']['return']

    def niSwitch_WaitForDebounce(self, vi, maximum_time_ms):  # noqa: N802
        if self._defaults['WaitForDebounce']['return'] != 0:
            return self._defaults['WaitForDebounce']['return']
        return self._defaults['WaitForDebounce']['return']

    def niSwitch_WaitForScanComplete(self, vi, maximum_time_ms):  # noqa: N802
        if self._defaults['WaitForScanComplete']['return'] != 0:
            return self._defaults['WaitForScanComplete']['return']
        return self._defaults['WaitForScanComplete']['return']

    def niSwitch_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niSwitch_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niSwitch_error_message", param='errorMessage')
        a = self._defaults['error_message']['errorMessage']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(error_message), len(a))):
            error_message[i] = a[i]
        return self._defaults['error_message']['return']

    def niSwitch_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niSwitch_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niSwitch_self_test", param='selfTestResult')
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niSwitch_self_test", param='selfTestMessage')
        a = self._defaults['self_test']['selfTestMessage']
        import sys
        if sys.version_info.major > 2 and type(a) is str:
            a = a.encode('ascii')
        for i in range(min(len(self_test_message), len(a))):
            self_test_message[i] = a[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niSwitch_AbortScan.side_effect = MockFunctionCallError("niSwitch_AbortScan")
        mock_library.niSwitch_AbortScan.return_value = 0
        mock_library.niSwitch_CanConnect.side_effect = MockFunctionCallError("niSwitch_CanConnect")
        mock_library.niSwitch_CanConnect.return_value = 0
        mock_library.niSwitch_Commit.side_effect = MockFunctionCallError("niSwitch_Commit")
        mock_library.niSwitch_Commit.return_value = 0
        mock_library.niSwitch_ConfigureScanList.side_effect = MockFunctionCallError("niSwitch_ConfigureScanList")
        mock_library.niSwitch_ConfigureScanList.return_value = 0
        mock_library.niSwitch_ConfigureScanTrigger.side_effect = MockFunctionCallError("niSwitch_ConfigureScanTrigger")
        mock_library.niSwitch_ConfigureScanTrigger.return_value = 0
        mock_library.niSwitch_Connect.side_effect = MockFunctionCallError("niSwitch_Connect")
        mock_library.niSwitch_Connect.return_value = 0
        mock_library.niSwitch_ConnectMultiple.side_effect = MockFunctionCallError("niSwitch_ConnectMultiple")
        mock_library.niSwitch_ConnectMultiple.return_value = 0
        mock_library.niSwitch_Disable.side_effect = MockFunctionCallError("niSwitch_Disable")
        mock_library.niSwitch_Disable.return_value = 0
        mock_library.niSwitch_Disconnect.side_effect = MockFunctionCallError("niSwitch_Disconnect")
        mock_library.niSwitch_Disconnect.return_value = 0
        mock_library.niSwitch_DisconnectAll.side_effect = MockFunctionCallError("niSwitch_DisconnectAll")
        mock_library.niSwitch_DisconnectAll.return_value = 0
        mock_library.niSwitch_DisconnectMultiple.side_effect = MockFunctionCallError("niSwitch_DisconnectMultiple")
        mock_library.niSwitch_DisconnectMultiple.return_value = 0
        mock_library.niSwitch_GetAttributeViBoolean.side_effect = MockFunctionCallError("niSwitch_GetAttributeViBoolean")
        mock_library.niSwitch_GetAttributeViBoolean.return_value = 0
        mock_library.niSwitch_GetAttributeViInt32.side_effect = MockFunctionCallError("niSwitch_GetAttributeViInt32")
        mock_library.niSwitch_GetAttributeViInt32.return_value = 0
        mock_library.niSwitch_GetAttributeViReal64.side_effect = MockFunctionCallError("niSwitch_GetAttributeViReal64")
        mock_library.niSwitch_GetAttributeViReal64.return_value = 0
        mock_library.niSwitch_GetAttributeViString.side_effect = MockFunctionCallError("niSwitch_GetAttributeViString")
        mock_library.niSwitch_GetAttributeViString.return_value = 0
        mock_library.niSwitch_GetChannelName.side_effect = MockFunctionCallError("niSwitch_GetChannelName")
        mock_library.niSwitch_GetChannelName.return_value = 0
        mock_library.niSwitch_GetError.side_effect = MockFunctionCallError("niSwitch_GetError")
        mock_library.niSwitch_GetError.return_value = 0
        mock_library.niSwitch_GetPath.side_effect = MockFunctionCallError("niSwitch_GetPath")
        mock_library.niSwitch_GetPath.return_value = 0
        mock_library.niSwitch_GetRelayCount.side_effect = MockFunctionCallError("niSwitch_GetRelayCount")
        mock_library.niSwitch_GetRelayCount.return_value = 0
        mock_library.niSwitch_GetRelayName.side_effect = MockFunctionCallError("niSwitch_GetRelayName")
        mock_library.niSwitch_GetRelayName.return_value = 0
        mock_library.niSwitch_GetRelayPosition.side_effect = MockFunctionCallError("niSwitch_GetRelayPosition")
        mock_library.niSwitch_GetRelayPosition.return_value = 0
        mock_library.niSwitch_InitWithTopology.side_effect = MockFunctionCallError("niSwitch_InitWithTopology")
        mock_library.niSwitch_InitWithTopology.return_value = 0
        mock_library.niSwitch_InitiateScan.side_effect = MockFunctionCallError("niSwitch_InitiateScan")
        mock_library.niSwitch_InitiateScan.return_value = 0
        mock_library.niSwitch_RelayControl.side_effect = MockFunctionCallError("niSwitch_RelayControl")
        mock_library.niSwitch_RelayControl.return_value = 0
        mock_library.niSwitch_ResetWithDefaults.side_effect = MockFunctionCallError("niSwitch_ResetWithDefaults")
        mock_library.niSwitch_ResetWithDefaults.return_value = 0
        mock_library.niSwitch_RouteScanAdvancedOutput.side_effect = MockFunctionCallError("niSwitch_RouteScanAdvancedOutput")
        mock_library.niSwitch_RouteScanAdvancedOutput.return_value = 0
        mock_library.niSwitch_RouteTriggerInput.side_effect = MockFunctionCallError("niSwitch_RouteTriggerInput")
        mock_library.niSwitch_RouteTriggerInput.return_value = 0
        mock_library.niSwitch_SendSoftwareTrigger.side_effect = MockFunctionCallError("niSwitch_SendSoftwareTrigger")
        mock_library.niSwitch_SendSoftwareTrigger.return_value = 0
        mock_library.niSwitch_SetAttributeViBoolean.side_effect = MockFunctionCallError("niSwitch_SetAttributeViBoolean")
        mock_library.niSwitch_SetAttributeViBoolean.return_value = 0
        mock_library.niSwitch_SetAttributeViInt32.side_effect = MockFunctionCallError("niSwitch_SetAttributeViInt32")
        mock_library.niSwitch_SetAttributeViInt32.return_value = 0
        mock_library.niSwitch_SetAttributeViReal64.side_effect = MockFunctionCallError("niSwitch_SetAttributeViReal64")
        mock_library.niSwitch_SetAttributeViReal64.return_value = 0
        mock_library.niSwitch_SetAttributeViString.side_effect = MockFunctionCallError("niSwitch_SetAttributeViString")
        mock_library.niSwitch_SetAttributeViString.return_value = 0
        mock_library.niSwitch_SetContinuousScan.side_effect = MockFunctionCallError("niSwitch_SetContinuousScan")
        mock_library.niSwitch_SetContinuousScan.return_value = 0
        mock_library.niSwitch_SetPath.side_effect = MockFunctionCallError("niSwitch_SetPath")
        mock_library.niSwitch_SetPath.return_value = 0
        mock_library.niSwitch_WaitForDebounce.side_effect = MockFunctionCallError("niSwitch_WaitForDebounce")
        mock_library.niSwitch_WaitForDebounce.return_value = 0
        mock_library.niSwitch_WaitForScanComplete.side_effect = MockFunctionCallError("niSwitch_WaitForScanComplete")
        mock_library.niSwitch_WaitForScanComplete.return_value = 0
        mock_library.niSwitch_close.side_effect = MockFunctionCallError("niSwitch_close")
        mock_library.niSwitch_close.return_value = 0
        mock_library.niSwitch_error_message.side_effect = MockFunctionCallError("niSwitch_error_message")
        mock_library.niSwitch_error_message.return_value = 0
        mock_library.niSwitch_reset.side_effect = MockFunctionCallError("niSwitch_reset")
        mock_library.niSwitch_reset.return_value = 0
        mock_library.niSwitch_self_test.side_effect = MockFunctionCallError("niSwitch_self_test")
        mock_library.niSwitch_self_test.return_value = 0
