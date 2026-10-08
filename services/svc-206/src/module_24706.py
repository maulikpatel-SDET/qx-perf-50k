"""Service module 24706: business logic, no crypto."""


def calculate_total_24706(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24706():
    return 'module 24706 handles orders and invoices'
