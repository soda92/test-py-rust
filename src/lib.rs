#[no_mangle]
pub extern "C" fn rust_function() {
    println!("Rust function called");
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
