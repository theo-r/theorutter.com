import * as React from "react"
import { graphql } from "gatsby"

import Bio from "../components/bio"
import Layout from "../components/layout"

const CV = ({ data, location }) => {
    const siteTitle = data.site.siteMetadata?.title || `Title`
    return (
        <Layout location={location} title={siteTitle}>
            I am a software engineer with over 5 years of experience designing and building enterprise scale data applications
            in AWS and Azure.
            <h2>Experience</h2>
            Oct 2021 - Present
            <br></br>
            <strong>Software Engineer - Data Security</strong> at bp
            <ul>
                <li>
                    Wrote and presented multiple design decisions related to IAM, Networking and Data Security
                    to the bp enterprise design forum as phase one of a large scale migration with over 50 KDDs.
                </li>
                <li>
                    Led a project demonstrating how a streaming ingestion of networking data 
                    could be migrated to Databricks to save more than £100k per year.
                </li>
                <li>
                    Mentored junior engineers and managed their workloads.
                </li>
                <li>
                    Developed re-usable components for DevSecOps pipelines saving time for 4 developer teams.
                </li>
            </ul>
            Oct 2020 - Sep 2021
            <br></br>
            <strong>Data Engineer</strong> at Elastacloud
            <ul>
                <li>
                    Developed CI/CD pipelines for Python applications with stages for 
                    linting, unit tests, SAST and SCA with Checkmarx and deployment to Azure
                </li>
                <li>
                    Refactored an AWS microservice to use step functions instead of independent scheduled 
                    steps; the refactor reduced the average time to run from hours to 
                    minutes while making the service easier to understand and maintain
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
                  Github Actions. <a href="https://hotspot.streamlit.app">Link here.</a>
                </li>
            </ul>
            <h2>Education</h2>
            Sep 2015 - Jul 2019
            <br></br>
            <strong>University of Nottingham</strong>
            <br></br>
            <i>Integrated Master's in Mathematics and Statistics (First Class)</i>
            <h2>Skills</h2>
            <p>Python, C#, Powershell, Bash, AWS, Azure, Azure Devops Pipelines, IaC (Terraform, Cloudformation, Bicep), Docker, Git, Linux, PowerBI</p>
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