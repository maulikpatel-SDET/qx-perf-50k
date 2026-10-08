"""Service module 28772: business logic, no crypto."""


def calculate_total_28772(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28772():
    return 'module 28772 handles orders and invoices'
