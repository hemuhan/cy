//
//  ViewController.m
//  cy_client
//
//  Created by hemuhan on 14-10-6.
//  Copyright (c) 2014年 hemuhan. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    self.view.backgroundColor = [UIColor colorWithRed:32 green:20 blue:50 alpha:1];
    UILabel *label1 = [[UILabel alloc] initWithFrame:CGRectMake(0, 0, 100, 40)];
    label1.text = @"你好么";
    label1.backgroundColor = [UIColor clearColor];
    [self.view addSubview:label1];
    
    NSString *s = @"http://192.168.31.167:8000/product/getStyle";
    NSURL *url = [NSURL URLWithString:s];
    NSURLRequest *request = [NSURLRequest requestWithURL:url];
    NSOperationQueue *queue = [NSOperationQueue mainQueue];
    [NSURLConnection sendAsynchronousRequest:request queue:queue completionHandler:^(NSURLResponse *response, NSData *data, NSError *connectionError) {
        if(data){
            NSString *datastr = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
            NSLog(@"%@",datastr);
            NSHTTPURLResponse *myresponse = (NSHTTPURLResponse*)response;
            NSLog(@"%d",[myresponse statusCode]);
        }else{
            NSLog(@"%@",connectionError);
        }
    }];
    
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
