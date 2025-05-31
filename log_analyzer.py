import re
from collections import defaultdict

def analyze_log(input_file="log.txt", output_file="rapport.txt"):
    """
    Analyse un fichier de logs et compte les occurrences de ERROR, WARNING, INFO.
    Args:
        input_file (str): Chemin du fichier de logs. Par défaut : "log.txt".
        output_file (str): Chemin du fichier de sortie. Par défaut : "rapport.txt".
    """
    log_counts = defaultdict(int)  # Dictionnaire pour compter les logs

    try:
        # Ouvrir le fichier de logs en mode lecture
        with open(input_file, 'r') as file:
            for line in file:
                if re.search(r'\bERROR\b', line, re.IGNORECASE):
                    log_counts["ERROR"] += 1
                elif re.search(r'\bWARNING\b', line, re.IGNORECASE):
                    log_counts["WARNING"] += 1
                elif re.search(r'\bINFO\b', line, re.IGNORECASE):
                    log_counts["INFO"] += 1

        with open(output_file, 'w') as file:
            file.write("=== STATISTIQUES DES LOGS ===\n")
            for level, count in log_counts.items():
                file.write(f"{level}: {count}\n")

        print(f"Analyse terminée. Résultats sauvegardés dans {output_file}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} n'existe pas.")

if __name__ == "__main__":
    analyze_log()