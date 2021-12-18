pipeline {

    agent any

    stages {
        stage('Run') {

            steps {
                sh 'pip install pytest'
                sh 'pytest -m "Sanity"'
            }
        }
    }
}
