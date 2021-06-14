$src=$args[0]
$dst=$args[1]
write-host $src
write-host $dst
write-host "https://source2021w4wv4gjwz2qes.blob.core.windows.net/mysrccontainer/$($args[0])?sv=2020-02-10&ss=bfqt&srt=sco&sp=rwdlacupx&se=2021-06-14T01:30:45Z&st=2021-06-13T17:30:45Z&spr=https&sig=SipWMJk7PPtrq9EeXcCpuOY6gCpGLoA5RVoZkzKuJZ8%3D"
write-host "https://dest2021w4wv4gjwz2qes.blob.core.windows.net/mydstcontainer/$($args[1])?sv=2020-02-10&ss=bfqt&srt=sco&sp=rwdlacuptfx&se=2021-06-14T01:36:52Z&st=2021-06-13T17:36:52Z&spr=https&sig=1dnm8CkNjSosG2utKYk52Dr0GJqePzj5P%2BmebVecQPY%3D"
./azcopy.exe cp "https://source2021w4wv4gjwz2qes.blob.core.windows.net/mysrccontainer/$($args[0])?sv=2020-02-10&ss=bfqt&srt=sco&sp=rwdlacupx&se=2021-06-14T01:30:45Z&st=2021-06-13T17:30:45Z&spr=https&sig=SipWMJk7PPtrq9EeXcCpuOY6gCpGLoA5RVoZkzKuJZ8%3D" "https://dest2021w4wv4gjwz2qes.blob.core.windows.net/mydstcontainer/$($args[1])?sv=2020-02-10&ss=bfqt&srt=sco&sp=rwdlacuptfx&se=2021-06-14T01:36:52Z&st=2021-06-13T17:36:52Z&spr=https&sig=1dnm8CkNjSosG2utKYk52Dr0GJqePzj5P%2BmebVecQPY%3D"