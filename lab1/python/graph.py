import pandas as pd
import matplotlib.pyplot as plt
import os

method_names = [
    "sum",
    "sum_omp_reduce",
    "sum_round_robin",
    "sum_round_robin_aligned",
    "sum_seq",
    "vector_sum_la",
    "sum_spp_cs",
    "sum_mutex",
    "sum_barrier"
]

output_dir = '../results/graphs'
os.makedirs(output_dir, exist_ok=True)

for method_name in method_names:
    input_csv = f'../results/csv/results_{method_name}.csv'
    if not os.path.exists(input_csv):
        print(f"Error: File '{input_csv}' not found.")
        continue

    data = pd.read_csv(input_csv)

    fig, axs = plt.subplots(3, figsize=(10, 15))

    axs[0].plot(data.index, data['Time (ms)'])
    axs[0].set_xlabel('Index')
    axs[0].set_ylabel('Time (ms)')
    axs[0].set_title('Time')
    axs[0].grid()

    axs[1].plot(data.index, data['Speedup'])
    axs[1].set_xlabel('Index')
    axs[1].set_ylabel('Speedup')
    axs[1].set_title('Speedup')
    axs[1].grid()

    axs[2].plot(data.index, data['Efficiency'])
    axs[2].set_xlabel('Index')
    axs[2].set_ylabel('Efficiency')
    axs[2].set_title('Efficiency')
    axs[2].grid()

    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'result_{method_name}_graphs.png'))

    print(f"Graphs for the method {method_name} saved in '{output_dir}'")