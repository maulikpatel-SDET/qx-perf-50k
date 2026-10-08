"""Service module 23235: business logic, no crypto."""


def calculate_total_23235(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23235():
    return 'module 23235 handles orders and invoices'
