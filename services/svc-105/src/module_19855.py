"""Service module 19855: business logic, no crypto."""


def calculate_total_19855(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19855():
    return 'module 19855 handles orders and invoices'
