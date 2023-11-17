from lxml import html
from urllib.parse import urlparse
import os
import requests

html_content = """
<table class="table-hover table-striped" id="mytable_courses">
                <thead class="primary-bg">
                    <tr>                      
                      <th scope="col">S.No</th>
                      <!--<th scope="col">Posted Date</th>-->
                       <!--<th scope="col">Course</th>-->
                       <th scope="col">Topic</th>
                      <th scope="col">Notes</th>
                      <th scope="col">Backup Video</th>
                      <!--<th scope="col">Comments</th>-->
                     
                    </tr>
                  </thead>
                  <tbody>
                    
                                         <tr>
                      <td data-label="S.No"><span class="course-txt">1</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">30-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">What we covered - course summary</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/345888946_1675048133.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">2</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">30-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">DevOps Interview Questions</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/127557922_1675048096.pdf" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">3</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">30-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">AWS Interview Questions</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/105583712_1675047982.pdf" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">4</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">25-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">DevOps Self Introduction</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/134797291_1674615497.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">5</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">24-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Agile + JIRA Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/787995812_1674568069.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">6</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">20-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Cloud Formation</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1768742084_1674182261.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">7</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">19-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">AWS Lambdas</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/476971865_1674097736.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">8</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">16-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">EFS Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1337806924_1673834929.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">9</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">10-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Terraform Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/961475687_1673372836.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">10</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">07-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">VPC Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/787308407_1673320219.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">VPC Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">11</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">04-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Cloud Watch and SNS</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/2098051775_1672800400.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Cloud Watch and SNS</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">12</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">03-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Elastic Beanstalk Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1189766160_1672715503.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">13</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">02-Jan</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Route 53 Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1437658379_1672628898.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">14</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">29-Dec</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">AWS S3 Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/909769136_1672282625.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">15</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">28-Dec</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">AWS IAM Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/880720401_1672195686.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">16</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">28-Dec</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">AWS RDS</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/627408515_1672195040.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">17</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">21-Dec</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Docker + K8S - Fullstack Project Setup</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1722211026_1671588862.pdf" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">18</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">20-Dec</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">EKS Cluster</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1517371960_1671505285.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">19</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">19-Dec</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">K8S Class Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/727242300_1671419350.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">20</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">17-Dec</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">HELM Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1485438570_1671281476.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">21</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">17-Dec</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">K8S Monitoring Tools</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/125967555_1671281060.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">22</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">07-Dec</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Kubernetes Cluster Setup (Kubeadm)</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/1712203981_1670382894.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Kubernetes Cluster Setup (Kubeadm)</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">23</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">23-Nov</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Docker Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/1312201403_1670040792.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Docker Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">24</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">22-Nov</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Ansible Roles</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/455670692_1669085386.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">25</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">15-Nov</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Ansible Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/1625615266_1669085061.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Ansible Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">26</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">14-Nov</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Application Environments</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/897642700_1668393683.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">27</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">11-Nov</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">DevOps Project - 1 (Setup)</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/603857269_1668135194.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">28</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">02-Nov</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Jenkins Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/1977786198_1667788639.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Jenkins Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">29</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">01-Nov</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Sonar Qube Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/2116411339_1667271462.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">30</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">28-Oct</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Apache Tomcat Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1664006515_1666925759.pdf" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">31</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">20-Oct</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Git Hub Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/7961493_1666753367.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Git Hub Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">32</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">15-Oct</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Nexus Class Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/1609426970_1666062238.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Nexus Class Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">33</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">13-Oct</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Maven Class Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/588986855_1665631435.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Maven Class Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">34</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">12-Oct</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">DevOps Tools Overview</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/733203259_1665573112.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">35</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">11-Oct</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Recover EC2 VM </span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1424241919_1665456996.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">36</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">08-Oct</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">EC2 Interview Questions</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/781287685_1665232057.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">37</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">03-Oct</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">EBS Volumes Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/138621160_1664765940.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt"></span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">38</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">29-Sep</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Windows VM Launching - EC2</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/693139742_1664433296.pdf" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Windows VM Launching - EC2</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">39</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">27-Sep</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">EC2 Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/947964234_1664247324.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">EC2 Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">40</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">27-Sep</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Cloud Computing Introduction</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1419501397_1664247308.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Cloud Computing Introduction</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">41</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">24-Sep</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Shell Scripting</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/599619622_1663994047.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Shell Scripting</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">42</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">21-Sep</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">Linux Running Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/./uploads/notes/1691263481_1663901486.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">Linux Running Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">43</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">19-Sep</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">DevOps Introduction Notes</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1589414158_1663555364.txt" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">DevOps Introduction Notes</span></td>-->
                     
                    </tr>

                 
                                           <tr>
                      <td data-label="S.No"><span class="course-txt">44</span></td>
                      <!--<td data-label="Posted Date"><span class="course-txt">15-Sep</span></td>-->
                      <!-- <td data-label="Course"><span class="course-txt">DevOps with AWS [06-DevOps- AWS-7 AM-7-Sept-FA]</span></td>-->
                      <td data-label="Topic"><span class="course-txt">AWS Account Creation</span></td>
                      
                                               
                      <td data-label="Notes"><span class="course-txt"><a href="https://ashokitech.com/uploads/notes/1217517611_1663209945.pdf" target="_blank" previewlistener="true">Download</a></span></td>
                                             
                      
                       <td data-label="Video Url"><a href="https://sso.teachable.com/secure/1400146/identity/login/password" target="_blank" previewlistener="true">Watch Video</a></td>
                                             <!--<td data-label="Comments"><span class="course-txt">AWS Account Creation</span></td>-->
                     
                    </tr>

                 
                                       
                                    
                  </tbody>
                </table>
"""

tree = html.fromstring(html_content)

file_names = tree.xpath('//table[@id="mytable_courses"]//td[@data-label="Topic"]//span/text()')
file_links = tree.xpath('//table[@id="mytable_courses"]//td[@data-label="Notes"]//a/@href')

files = dict(zip(file_names, file_links))

output_folder = 'notes'

os.makedirs(output_folder, exist_ok=True)

for index, (file_name, file_link) in enumerate(files.items(), start=1):
    file_name = file_name.replace(' ', '_')
    url_path = urlparse(file_link).path
    file_extension = os.path.splitext(url_path)[1].lstrip('.')
    output_path = os.path.join(output_folder, f'{index}_{file_name}.{file_extension}')
    response = requests.get(file_link)
    if response.status_code == 200:
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded '{file_name}' to '{output_path}'")
    else:
        print(f"Failed to download '{file_name}'. Status code: {response.status_code}")