import * as React from "react"
import { Link, graphql } from "gatsby"

import Bio from "../components/bio"
import Layout from "../components/layout"

const CV = ({ data, location }) => {
    const siteTitle = data.site.siteMetadata?.title || `Title`
    return (
        <Layout location={location} title={siteTitle}>
            <h2>Experience</h2>
            Oct 2021 - Present
            <br></br>
            <strong>Application Security Engineer</strong> at BP
            <ul>
                <li>
                    Worked in a cross functional role providing security assurance,
                    engineering and design services for product teams building
                    cloud data platforms in AWS and Azure while owning and delivering
                    security features on the platforms.
                </li>
                <li>
                    Developed numerous build and deployment pipelines for Python
                    and C# serverless applications in Azure DevOps and helped
                    design and standardize a CI/CD framework to include automated
                    SAST and SCA.
                </li>
                <li>
                    Prepared and delivered presentations and technical 
                    demonstrations for customers and senior leadership teams.
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