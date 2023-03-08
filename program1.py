import wmi

wmiService = wmi.WMI()


def isAnyAdapterEnabled():
    adapters = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    return len(adapters) > 0


def getEnabledAdapters():
    adapters = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    return [{"Index": adapter.Index, "Name": adapter.Caption} for adapter in adapters]


def disableAllAdapters():
    adapters = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    adapterStates = []
    for adapter in adapters:
        adapterStates.append({"Index": adapter.Index, "Enabled": adapter.Enabled})
        adapter.Disable()
    return adapterStates


def enableAllAdapters(adapterStates):
    for adapterState in adapterStates:
        adapter = wmiService.Win32_NetworkAdapterConfiguration(Index=adapterState["Index"])[0]
        if not adapterState["Enabled"]:
            adapter.Enable()
    return adapterStates


if __name__ == "__main__":
    
    print(isAnyAdapterEnabled())

    
    adapters = getEnabledAdapters()
    for adapter in adapters:
        print(f'Index: {adapter["Index"]}, Name: {adapter["Name"]}')

    
    adapterStates = disableAllAdapters()
    for adapterState in adapterStates:
        print(f'Adapter {adapterState["Index"]} was {"enabled" if adapterState["Enabled"] else "disabled"}')
        
    
    enableAllAdapters(adapterStates)
