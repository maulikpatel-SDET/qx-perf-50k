"""Service module 27700: business logic, no crypto."""


def calculate_total_27700(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27700():
    return 'module 27700 handles orders and invoices'
