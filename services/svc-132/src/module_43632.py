"""Service module 43632: business logic, no crypto."""


def calculate_total_43632(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43632():
    return 'module 43632 handles orders and invoices'
