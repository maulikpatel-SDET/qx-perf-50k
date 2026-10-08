"""Service module 33946: business logic, no crypto."""


def calculate_total_33946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33946():
    return 'module 33946 handles orders and invoices'
