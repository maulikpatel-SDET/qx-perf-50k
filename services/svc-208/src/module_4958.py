"""Service module 4958: business logic, no crypto."""


def calculate_total_4958(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4958():
    return 'module 4958 handles orders and invoices'
