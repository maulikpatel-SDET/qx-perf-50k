"""Service module 19392: business logic, no crypto."""


def calculate_total_19392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19392():
    return 'module 19392 handles orders and invoices'
