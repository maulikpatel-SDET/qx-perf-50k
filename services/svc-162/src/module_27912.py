"""Service module 27912: business logic, no crypto."""


def calculate_total_27912(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27912():
    return 'module 27912 handles orders and invoices'
