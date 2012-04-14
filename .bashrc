function please() {
    case "$1" in
        start) ./webroot.py;;
        open) open http://localhost:5000;;
        *) echo "no such command: $1";;
    esac
}
alias plz="please"
