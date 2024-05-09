import requests
from bs4 import BeautifulSoup

def get_latest_version(url, selector):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            latest_version = soup.select_one(selector).text.strip()
            return latest_version
        else:
            print(f"Failed to fetch {url}. Status code:", response.status_code)
            return None
    except Exception as e:
        print("Error occurred:", e)
        return None

# Dictionary mapping application names to their corresponding URLs and CSS selectors
applications = {
    "Spring-Boot": ("https://spring.io/projects/spring-boot", '.tag.is-primary'),
    "Nodejs": ("https://endoflife.date/nodejs", '.lifecycle .release:nth-of-type(2) td:nth-of-type(5) a'),
    "MySQL-8": ("https://endoflife.date/mysql", '.lifecycle .release:nth-of-type(4) td:nth-of-type(5) a'),
    "JDK": ("https://endoflife.date/oracle-jdk", '.lifecycle .release:nth-of-type(2) td:nth-of-type(5) a'),
    "PHP": ("https://endoflife.date/php", '.lifecycle .release:nth-of-type(2) td:nth-of-type(5) a'),
    "Apache-Spark": ("https://endoflife.date/apache-spark", '.lifecycle .release:nth-of-type(1) td:nth-of-type(4) a'),
    "MongoDB": ("https://endoflife.date/mongodb", '.lifecycle .release:nth-of-type(8) td:nth-of-type(4) a'),
    "MongoDB": ("https://endoflife.date/mongodb", '.lifecycle .release:nth-of-type(8) td:nth-of-type(4) a'),
    "OpenSSL": ("https://endoflife.date/openssl", '.lifecycle .release:nth-of-type(4) td:nth-of-type(5) a'),
    "Oracle-Linux": ("https://endoflife.date/oracle-linux", '.lifecycle .release:nth-of-type(2) td:nth-of-type(5) a'),
    "Apache Tomcat": ("https://endoflife.date/tomcat", '.lifecycle .release:nth-of-type(1) td:nth-of-type(4) a'),
    "Apache ActiveMQ": ("https://endoflife.date/apache-activemq", '.lifecycle .release:nth-of-type(3) td:nth-of-type(4) a'),
    "Apache Struts": ("https://endoflife.date/apache-struts", '.lifecycle .release:nth-of-type(1) td:nth-of-type(4) a'),
    "Apache Hadoop": ("https://endoflife.date/apache-hadoop", '.lifecycle .release:nth-of-type(1) td:nth-of-type(4) a'),
    "Apache ZooKeeper": ("https://endoflife.date/zookeeper", '.lifecycle .release:nth-of-type(2) td:nth-of-type(5) a'),
    "Apache Log4j": ("https://endoflife.date/log4j", '.lifecycle .release:nth-of-type(1) td:nth-of-type(4) a'),
    "Apache HTTP Server": ("https://endoflife.date/apache", '.lifecycle .release:nth-of-type(1) td:nth-of-type(4) a'),
    "Ruby": ("https://endoflife.date/ruby", '.lifecycle .release:nth-of-type(1) td:nth-of-type(4) a'),
}
print(f"Latest version of Application are :")
# Fetch latest versions for each application
for app, (url, selector) in applications.items():
    latest_version = get_latest_version(url, selector)
    if latest_version:
       
        print(f" {app}: {latest_version}")
