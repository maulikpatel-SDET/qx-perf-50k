"""Service module 36957: business logic, no crypto."""


def calculate_total_36957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36957():
    return 'module 36957 handles orders and invoices'
