from leitor_de_dados import LeitorDeDados

def main():
    # Instantiate the LeitorDeDados with the GitHub API URL
    leitor_de_dados = LeitorDeDados("https://api.github.com/repos/rafaelcerqueira/dados-matriculas-eja/git/trees/main/dados-censo-educacao/Salvador?recursive=1")
    
    # Read the scripts
    scripts_content = leitor_de_dados.read_scripts()

    # Print the content of each script
    for content in scripts_content:
        print(content)

if __name__ == "__main__":
    main()