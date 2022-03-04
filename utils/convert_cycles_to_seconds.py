def cpu_processing_time(cycles: int, freq: float):
    """
    :param cycles
    :param freq: MHz
    :return: seconds
    """
    return (cycles / (freq * pow(10, 6))) * pow(10,3)


if __name__ == '__main__':
    print(cpu_processing_time(1.05149 * pow(10, 6), 1300))
