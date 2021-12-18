pipeline {
    agent any

    stages {
        stage('Testing') {
            steps {
                sh '''
                ls
                cd ${WORKSPACE}
                pip install pytest
                '''
            }
        }

    }
}