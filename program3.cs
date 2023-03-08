using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Set up Chrome options to run in headless mode
        var chromeOptions = new ChromeOptions();
        chromeOptions.AddArgument("--headless");

    
        using (var driver = new ChromeDriver(chromeOptions))
        {

            driver.Navigate().GoToUrl("https://www.emsisoft.com/en/anti-malware-home/");

            
            IWebElement alternativeOptionsButton = driver.FindElement(By.XPath("//a[contains(text(),'Alternative installation options')]"));
            alternativeOptionsButton.Click();

            
            IWebElement webInstallerButton = driver.FindElement(By.XPath("//a[contains(text(),'Web installer')]"));
            webInstallerButton.Click();

            string downloadUrl = driver.Url;
            WebClient webClient = new WebClient();
            webClient.DownloadFile(downloadUrl, "emsisoft_web_installer.exe");
        }
    }
}
