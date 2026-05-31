import argparse
from src.population_model import run_experiment


def parse_args():
    parser = argparse.ArgumentParser(description='Run population dynamics experiment and save a figure.')
    parser.add_argument('--output-dir', default='figures', help='Directory to save the output image')
    parser.add_argument('--output-file', default='eksperimenti_1.png', help='Output image filename')
    parser.add_argument('--time', type=float, default=500.0, help='Total simulation time')
    parser.add_argument('--steps', type=int, default=1000, help='Number of time steps')
    parser.add_argument('--show', action='store_true', help='Show the figure after saving')
    return parser.parse_args()


def main():
    args = parse_args()
    output_path = run_experiment(
        output_dir=args.output_dir,
        output_file=args.output_file,
        total_time=args.time,
        num_steps=args.steps,
    )
    print(f'Figure saved to: {output_path}')
    if args.show:
        from PIL import Image
        img = Image.open(output_path)
        img.show()


if __name__ == '__main__':
    main()
