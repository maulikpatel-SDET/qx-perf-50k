"""Service module 12235: business logic, no crypto."""


def calculate_total_12235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12235():
    return 'module 12235 handles orders and invoices'
