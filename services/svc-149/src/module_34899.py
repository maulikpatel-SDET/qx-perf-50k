"""Service module 34899: business logic, no crypto."""


def calculate_total_34899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34899():
    return 'module 34899 handles orders and invoices'
