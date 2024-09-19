pipeline {
    agent any
    tools {
        jdk 'jdk17'
        maven 'maven3'
    }
    
    environment {
        SCANNER_HOME= tool  'sonar-scanner'
    }
    
    stages {
        stage('git checkout') {
            steps {
                git branch: 'main', credentialsId: 'git-cred', url: 'https://github.com/VinayK05/FullStack-Blogging-App1.git'
            }
        }
        stage('compile') {
            steps {
                sh "mvn compile"
            }
        }
        stage('test') {
            steps {
                sh "mvn test"
            }
        }
        stage('trivy fs scan') {
            steps {
                sh "trivy fs --format table -o fs.html ."
            }
        }
        stage('sonarqube analysis') {
            steps {
                withSonarQubeEnv('sonar-server') {
                sh '''$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=Blogging-App -Dsonar.projectKey=Blogging-App \
                      -Dsonar.java.binaries=target'''
                }
                
            }
        }
        stage('build') {
            steps {
                sh "mvn package"
            }
        }
        stage('publish artifacts') {
            steps {
                withMaven(globalMavenSettingsConfig: 'maven-settings', jdk: 'jdk17', maven: 'maven3', mavenSettingsConfig: '', traceability: true) {
                    sh "mvn deploy"
                }
                
            }
        }
        stage('hello') {
            steps {
                echo 'hello world'
            }
        }
        
        
        
        
    }
}
