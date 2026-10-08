"""Service module 14981: business logic, no crypto."""


def calculate_total_14981(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14981():
    return 'module 14981 handles orders and invoices'
