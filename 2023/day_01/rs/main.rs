use std::fs;
use std::collections::HashMap;
use std::time::Instant;

fn read_input(path: String) -> Vec<String> {
    fs::read_to_string(path)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}

fn sum_calibration_values(codes: &Vec<String>) -> u32 {
    let mut accum = 0;

    for code in codes.iter() {
        let mut fd = 0;
        let mut ld = 0;

        for chr in code.chars() {
            if chr.is_digit(10) {
                fd = chr.to_digit(10).unwrap();
                break;
            }
        }
        for chr in code.chars().rev() {
            if chr.is_digit(10) {
                ld = chr.to_digit(10).unwrap();
                break
            }
        }
        accum += fd * 10 + ld;
    }
    accum
}


fn sum_calibration_values_2(codes: &Vec<String>) -> u32 {
    let DIGITS: Vec<u32> = (1..10).collect();
    let DIGITS_MAP = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]);

    let mut accum = 0;
    for code in codes.iter() {
        let mut fd_found = HashMap::new();

        for d in DIGITS.iter() {
            let pos: usize = match code.find(d.to_string().as_str()) {
                Some(num) => num,
                None => continue,
            };
            fd_found.insert(pos, *d);
        }
        for name in DIGITS_MAP.keys() {
            let pos: usize = match code.find(name) {
                Some(num) => num,
                None => continue,
            };
            fd_found.insert(pos, DIGITS_MAP.get(name).copied().unwrap());
        }
        let min_pos = fd_found.keys().min().unwrap();
        let fd = fd_found.get(min_pos).unwrap();

        let mut ld_found = HashMap::new();
        for d in DIGITS.iter() {
            let pos: usize = match code.rfind(d.to_string().as_str()) {
                Some(num) => num,
                None => continue,
            };
            ld_found.insert(pos, *d);
        }
        for name in DIGITS_MAP.keys() {
            let pos: usize = match code.rfind(name) {
                Some(num) => num,
                None => continue,
            };
            ld_found.insert(pos, DIGITS_MAP.get(name).copied().unwrap());
        }
        let max_pos = ld_found.keys().max().unwrap();
        let ld = ld_found.get(max_pos).unwrap();

        accum += fd * 10 + ld;
    }
    accum
}

fn main() {
    let codes = read_input(String::from("../input.txt"));

    let rude_val = sum_calibration_values(&codes);
    println!("The sum of all of the calibration values: {}", rude_val);

    let now = Instant::now();
    let precise_val = sum_calibration_values_2(&codes);
    println!("The precise sum of all of the calibration values: {}", precise_val);
    println!("Time elapsed: {}", now.elapsed().as_nanos());
}