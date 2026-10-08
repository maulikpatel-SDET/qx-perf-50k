"""Service module 37115: business logic, no crypto."""


def calculate_total_37115(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37115():
    return 'module 37115 handles orders and invoices'
