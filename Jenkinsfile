pipeline {

    agent any

    stages {
        stage('Run') {

            steps {
                pip install pytest
                pytest -m 'Sanity'
            }
        }
    }
}
