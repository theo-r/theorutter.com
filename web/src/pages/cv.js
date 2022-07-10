import * as React from "react"
import { graphql } from "gatsby"

import Bio from "../components/bio"
import Layout from "../components/layout"

const CV = ({ data, location }) => {
    const siteTitle = data.site.siteMetadata?.title || `Title`
    return (
        <Layout location={location} title={siteTitle}>
            <h2>Experience</h2>
            Oct 2021 - Present
            <br></br>
            <strong>Security Engineer</strong> at bp
            <ul>
                <li>
                    Designed and implemented a new access control model for a project 
                    replacing write access for all developers with reduced privileges 
                    in higher environments. Created a repository to store developer 
                    access as code and automated the access granting process 
                    to remove bottlenecks on team leads
                </li>
                <li>
                    Led threat modelling sessions with development teams using the 
                    STRIDE framework to identify vulnerabilities in their designs
                </li>
                <li>
                    Performed code reviews for product teams and explained security best practices
                </li>
                <li>
                    Developed and maintained a service to rotate AWS IAM user secrets and synchronise 
                    them with applications in Azure Active Directory
                </li>
            </ul>
            Oct 2020 - Sep 2021
            <br></br>
            <strong>Cloud Engineer</strong> at Elastacloud
            <ul>
                <li>
                    Designed and implemented a new access control model for a project 
                    replacing write access for all developers with reduced privileges 
                    in higher environments. Created a repository to store developer 
                    access as code and automated the access granting process 
                    to remove bottlenecks on team leads
                </li>
                <li>
                    Led threat modelling sessions with development teams using the 
                    STRIDE framework to identify vulnerabilities in their designs
                </li>
                <li>
                    Created documentation on best practices for writing integration tests 
                    of serverless applications so that they can be integrated in CI/CD pipelines
                </li>
            </ul>
            <h2>Projects</h2>
            <ul>
                <li>
                  Created a web application reporting my Spotify listening habits. 
                  The app is deployed in AWS using a Lambda backend to refresh a 
                  Glue table hourly; the front end queries the table using Athena. 
                  The infrastructure is created with the AWS CDK and deployed using 
                  Github Actions. <a href="https://share.streamlit.io/theo-r/hotspot/hotspot/hotspot.py">Link here.</a>
                </li>
            </ul>
            <h2>Education</h2>
            Sep 2015 - Jul 2019
            <br></br>
            <strong>University of Nottingham</strong>
            <br></br>
            <i>Integrated Master's in Mathematics and Statistics (First Class)</i>
            <h2>Skills</h2>
            <ul>
                <li>Python</li>
                <li>C#</li>
                <li>Powershell</li>
                <li>Bash</li>
                <li>AWS</li>
                <li>Azure</li>
                <li>ADO YAML Pipelines</li>
                <li>IaC (Cloudformation, Bicep)</li>
                <li>Linux</li>
                <li>Git</li>
                <li>Docker</li>
            </ul>
            <Bio />
        </Layout>
    )
}

export default CV

export const pageQuery = graphql`
  query {
    site {
      siteMetadata {
        title
      }
    }
  }
`