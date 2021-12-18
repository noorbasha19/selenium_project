pipeline {
    agent any

    stages {
        stage('Testing') {
            steps {
                bat '''
                cd ${WORKSPACE}
                pip install pytest
                pytest -m 'Sanity'
                '''
            }
        }

    }
}