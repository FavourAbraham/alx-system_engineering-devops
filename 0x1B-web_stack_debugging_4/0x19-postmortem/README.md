Postmortem: Website Outage Due to Load Balancer Error
Issue Summary

Duration: August 21, 2024, 11:15 AM - 12:45 PM (UTC)
Impact: For 1 hour and 30 minutes, 85% of our users experienced slow loading times or couldn’t access our website. This affected our e-commerce platform, causing problems with orders and frustrating customers.
Root Cause: The problem was caused by a mistake in the load balancer settings, which made most traffic go to one server, overloading it.

Timeline
11:15 AM: The issue was detected by our monitoring system, which alerted us to slow response times and errors.
11:20 AM: The on-call engineer received the alert and started checking the server logs for problems.
11:25 AM: We first thought it was due to a sudden increase in traffic and tried adding more servers.
11:35 AM: When the problem didnt improve, we looked into how the network traffic was being handled.
11:45 AM: The network team found that the load balancer was misconfigured, sending most traffic to one server.
12:00 PM: We fixed the load balancer settings to spread the traffic evenly across all servers.
12:20 PM: Server performance improved, and the website began to recover.
12:45 PM: The issue was fully resolved, and the website was back to normal.
Root Cause and Resolution
Root Cause:
The load balancer was set up incorrectly due to a recent update. Instead of spreading traffic evenly across all servers, it sent most of it to just one server. This caused the server to become overloaded and slow down. The mistake happened because the update script had a bug.

Resolution:
We fixed the load balancer settings to distribute traffic properly. We also rolled back the faulty update and tested the settings in a non-live environment before making them live again.

Corrective and Preventative Measures
Improvements:

Review Load Balancer Changes: Ensure changes to load balancer settings are thoroughly checked and reviewed.
Better Monitoring: Set up monitoring to detect any uneven traffic distribution early.
Test Before Changes: Always test configuration changes in a non-live environment before applying them to the live system.
Tasks:

 Fix the update script to prevent similar errors.
 Set up monitoring to watch for uneven traffic distribution.
 Train engineers on how to properly configure load balancers.
 Implement a quick way to roll back changes if something goes wrong.
