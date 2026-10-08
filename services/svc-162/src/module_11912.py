"""Service module 11912: business logic, no crypto."""


def calculate_total_11912(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11912():
    return 'module 11912 handles orders and invoices'
