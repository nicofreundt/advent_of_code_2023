import re

FILE = "input.txt"

def parse_to_map(modules):
    return {(matches:=re.findall('[a-z]+', module))[0]: matches[1:] for module in modules}

if __name__ == "__main__":
    # part one
    with open(FILE) as file:
        module_list = file.read()
        broadcaster = parse_to_map(re.findall('broadcaster -> (?>[a-z]+, )*(?>[a-z]+)', module_list))
        flip_flops = parse_to_map(re.findall('%[a-z]+ -> (?>[a-z]+, )*(?>[a-z]+)', module_list))
        conjunctions = parse_to_map(re.findall('&[a-z]+ -> (?>[a-z]+, )*(?>[a-z]+)', module_list))
        active_flops = []
        all_modules = flip_flops.copy()
        all_modules.update(conjunctions)
        con_input = {con: {k: 0 for k, _ in filter(lambda x: con in x[1], all_modules.items())} for con in conjunctions}
        all_signals = [1000, 0]
        for _ in range(1000):
            cur_signals = [('broadcaster', 0, signal) for signal in broadcaster['broadcaster']]
            while cur_signals:
                last_module, pulse, cur_signal = cur_signals.pop(0)
                all_signals[pulse] += 1
                if cur_signal not in all_modules:
                    continue
                if cur_signal in conjunctions:
                    con_input[cur_signal][last_module] = pulse
                cur_modules = flip_flops[cur_signal] if cur_signal in flip_flops else conjunctions[cur_signal]
                if cur_signal in flip_flops and pulse == 0:
                        for module in cur_modules:
                            cur_signals.append((cur_signal, cur_signal not in active_flops, module))
                elif cur_signal in conjunctions:
                    if len(con_input[cur_signal]) == 1:
                        for module in cur_modules:
                            cur_signals.append((cur_signal, 0 if pulse else 1, module))
                    else:
                        if all(v for v in con_input[cur_signal].values()):
                            for module in cur_modules:
                                cur_signals.append((cur_signal, 0, module))
                        else:
                            for module in cur_modules:
                                cur_signals.append((cur_signal, 1, module))
                if last_module in flip_flops:
                    if pulse == 1:
                        active_flops.append(last_module)
                    elif pulse == 0:
                        active_flops.remove(last_module)
        print("Part 1:", all_signals[0] * all_signals[1])

    # part two 
    with open(FILE) as file:
        module_list = file.read()
        broadcaster = parse_to_map(re.findall('broadcaster -> (?>[a-z]+, )*(?>[a-z]+)', module_list))
        flip_flops = parse_to_map(re.findall('%[a-z]+ -> (?>[a-z]+, )*(?>[a-z]+)', module_list))
        conjunctions = parse_to_map(re.findall('&[a-z]+ -> (?>[a-z]+, )*(?>[a-z]+)', module_list))
        active_flops = []
        all_modules = flip_flops.copy()
        all_modules.update(conjunctions)
        con_input = {con: {k: 0 for k, _ in filter(lambda x: con in x[1], all_modules.items())} for con in conjunctions}
        pressed_button = 0
        no_low_rx = True
        module_before_rx = [k for k, _ in filter(lambda x: 'rx' in x[1], all_modules.items())][0]
        end_state = con_input[module_before_rx].copy()
        while no_low_rx:
            if all(val > 0 for val in end_state.values()):
                break
            pressed_button += 1
            cur_signals = [('broadcaster', 0, signal) for signal in broadcaster['broadcaster']]
            while cur_signals:
                last_module, pulse, cur_signal = cur_signals.pop(0)
                if last_module in con_input[module_before_rx] and pulse == 1:
                    end_state[last_module] = pressed_button
                if cur_signal not in all_modules:
                    if cur_signal == 'rx' and pulse == 0:
                        no_low_rx == False
                    continue
                if cur_signal in conjunctions:
                    con_input[cur_signal][last_module] = pulse
                cur_modules = flip_flops[cur_signal] if cur_signal in flip_flops else conjunctions[cur_signal]
                if cur_signal in flip_flops and pulse == 0:
                    for module in cur_modules:
                        cur_signals.append((cur_signal, cur_signal not in active_flops, module))
                elif cur_signal in conjunctions:
                    if len(con_input[cur_signal]) == 1:
                        for module in cur_modules:
                            cur_signals.append((cur_signal, 0 if pulse else 1, module))
                    else:
                        if all(v for v in con_input[cur_signal].values()):
                            for module in cur_modules:
                                cur_signals.append((cur_signal, 0, module))
                        else:
                            for module in cur_modules:
                                cur_signals.append((cur_signal, 1, module))
                if last_module in flip_flops:
                    if pulse == 1:
                        active_flops.append(last_module)
                    elif pulse == 0:
                        active_flops.remove(last_module)
        x, m, a, s = end_state.values()
        print("Part 2:", x*m*a*s)