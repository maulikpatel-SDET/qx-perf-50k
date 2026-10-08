"""Service module 30981: business logic, no crypto."""


def calculate_total_30981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30981():
    return 'module 30981 handles orders and invoices'
