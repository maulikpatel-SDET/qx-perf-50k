"""Service module 24946: business logic, no crypto."""


def calculate_total_24946(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24946():
    return 'module 24946 handles orders and invoices'
