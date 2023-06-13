# Reference:Chat GPT Assisted

# Script:   code challenge 11               
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 13,2023     
# Purpose:Create a Python script that fetches this information using Psutil:
#Time spent by normal processes executing in user mode
#Time spent by processes executing in kernel mode
#Time when system was idle
#Time spent by priority processes executing in user mode
#Time spent waiting for I/O to complete.
#Time spent for servicing hardware interrupts
#Time spent for servicing software interrupts
#Time spent by other operating systems running in a virtualized environment
#Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel


import psutil

# Time spent by normal processes executing in user mode
user_time = psutil.cpu_times().user

# Time spent by processes executing in kernel mode
kernel_time = psutil.cpu_times().system

# Time when system was idle
idle_time = psutil.cpu_times().idle

# Time spent by priority processes executing in user mode
priority_user_time = psutil.cpu_times().nice

# Time spent waiting for I/O to complete
io_wait_time = psutil.cpu_times().iowait

# Time spent for servicing hardware interrupts
interrupt_time = psutil.cpu_times().irq

# Time spent for servicing software interrupts
soft_interrupt_time = psutil.cpu_times().softirq

# Time spent by other operating systems running in a virtualized environment
steal_time = psutil.cpu_times().steal

# Time spent running a virtual CPU for guest operating systems
guest_time = psutil.cpu_times().guest

# Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel
guest_nice_time = psutil.cpu_times().guest_nice

# Print the fetched information
print("Time spent by normal processes executing in user mode:", user_time)
print("Time spent by processes executing in kernel mode:", kernel_time)
print("Time when system was idle:", idle_time)
print("Time spent by priority processes executing in user mode:", priority_user_time)
print("Time spent waiting for I/O to complete:", io_wait_time)
print("Time spent for servicing hardware interrupts:", interrupt_time)
print("Time spent for servicing software interrupts:", soft_interrupt_time)
print("Time spent by other operating systems running in a virtualized environment:", steal_time)
print("Time spent running a virtual CPU for guest operating systems:", guest_time)
print("Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel:", guest_nice_time)


