"""Service module 15471: business logic, no crypto."""


def calculate_total_15471(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15471():
    return 'module 15471 handles orders and invoices'
