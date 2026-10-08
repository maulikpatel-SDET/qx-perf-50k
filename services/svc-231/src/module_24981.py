"""Service module 24981: business logic, no crypto."""


def calculate_total_24981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24981():
    return 'module 24981 handles orders and invoices'
