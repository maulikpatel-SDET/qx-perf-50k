"""Service module 33981: business logic, no crypto."""


def calculate_total_33981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33981():
    return 'module 33981 handles orders and invoices'
