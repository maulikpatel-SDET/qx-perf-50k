"""Service module 27958: business logic, no crypto."""


def calculate_total_27958(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27958():
    return 'module 27958 handles orders and invoices'
