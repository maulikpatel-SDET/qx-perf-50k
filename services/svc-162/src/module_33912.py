"""Service module 33912: business logic, no crypto."""


def calculate_total_33912(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33912():
    return 'module 33912 handles orders and invoices'
