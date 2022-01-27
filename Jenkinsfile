import java.text.SimpleDateFormat

def currentDate() {
    def date = new Date()
    currentDate = new SimpleDateFormat('MM/dd/yy_HH:mm:ss')
    return currentDate.format(date).toString()
}

node("Win4jenkins4testers") { //имя сервера

    def branch = env.Branch // выбор ветки проекта
    def tagTest = env.Tag // SELECT smoke/regress/api/ui
    def unique = env.UniqueTest // STRING id unique test
    def browser = env.Browser // SELECT выбор браузера
    def ip = env.StandIP // SELECT выбор стенда
    def standVersion = env.StandVersion // SELECT version
    def headless = env.Headless // SELECT version


    stage("Prepare Project") {
        cleanWs()
    }

    stage("Cloning Project") {
        git branch: branch,
            credentialsId: 'orudenko-jenkins',
            url: 'http://gitlab.local/Tests/selenium-python-arm.git'
    }

    stage("Run Tests") {

        try {
            bat 'set PATH=C:\\Users\\jenkins\\AppData\\Local\\Programs\\Python\\Python39;%PATH%'
            bat 'python --version'
            bat 'python -m pip install -r requirements.txt'
            bat 'cd C:\\Jenkins\\workspace\\autotest\\runtest'
            tagTest = "-m $Tag"
            echo "$StandIP"
            echo "$Tag"
            if (unique != "-") {
                tagTest = " -m $UniqueTest"
            }
            bat 'pytest -s -q -v '+tagTest+' --alluredir=target/allure-results --disable-pytest-warnings --browser '+browser+' --ip '+ip+' --stand-version '+standVersion+' --headless '+headless
        } catch (Throwable ignore) { }
    }

    stage('Save Allure Results') {
            script {
                archiveArtifacts 'target/allure-results/*'
            }
    }

    stage('Allure Reports') {
        script {
            allure([
                commandline      : 'allure-2.8.0',
                includeProperties: true,
                jdk              : '',
                properties       : [],
                reportBuildPolicy: 'ALWAYS',
                results          : [[path: 'target/allure-results']]
            ])
        }
    }

     stage('Publish') {
        echo 'Publish Allure report'
        publishHTML(
                target: [
                        allowMissing         : false,
                        alwaysLinkToLastBuild: false,
                        keepAll              : true,
                        reportDir            : 'target/allure-results',
                        reportFiles          : 'index.html',
                        reportName           : "Allure Report"
                ]
        )
    }

    // Пофиксить отправку почтовых уведомлений
    stage('Email-notification') {

         emailext(
              body:   "Ghbdtn",
              subject: "На стенде 10.17.7.72:8443 завершился прогон тестов функционала SafeMobile с результатом: " + currentBuild.currentResult,
              to: env.EMAIL_ADDRESS_LIST
         )
    }
}
