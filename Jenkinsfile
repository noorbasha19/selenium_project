pipeline {

    agent any

    stages {
        stage('Run') {

            steps {
                sh 'pip install pytest'
                sh 'ls'
                sh 'pytest -m "Sanity"'
            }
        }
    }
}
