<?php

$client = new GearmanClient();
$client->addServer();
$status = $client->jobStatus($argv[1]);
printf("status: %d/%d\n", $status[2], $status[3]);

